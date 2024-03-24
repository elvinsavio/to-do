package controller

import (
	"context"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
	"time"

	"elvinsavio/todo/database"
	"elvinsavio/todo/types"

	"go.mongodb.org/mongo-driver/bson"
)

type Project struct {
	Name       string
	Theme      string
	CreatedAt  time.Time
	LastOpened time.Time
}

func (p *Project) NewProject() (bool, error) {
	prefix := os.Getenv("MONGO_PREFIX")
	if prefix == "" {
		return false, fmt.Errorf("MONGO_PREFIX not set")
	}

	p.Name = prefix + "-" + p.Name // Set project name

	client, err := database.GetClient()
	if err != nil {
		return false, fmt.Errorf("failed to connect to db: %v", err.Error())
	}

	// Check if the project already exists
	databases, err := client.ListDatabaseNames(context.Background(), bson.D{})
	if err != nil {
		return false, fmt.Errorf("failed to list database names: %v", err.Error())
	}

	for _, db := range databases {
		if db == p.Name {
			return false, fmt.Errorf("%s already exists", p.Name)
		}
	}

	// Create new project and add default settings
	collection := client.Database(p.Name).Collection("settings")

	settings := bson.D{
		{Key: "Theme", Value: p.Theme},
		{Key: "CreatedAt", Value: p.CreatedAt},
		{Key: "LastOpened", Value: p.LastOpened},
	}

	if _, err := collection.InsertOne(context.Background(), settings); err != nil {
		return false, fmt.Errorf("failed to insert default settings: %v", err.Error())
	}

	return true, nil
}

func (p *Project) GetAllProjects(limit int) ([]types.ProjectList, error) {
	prefix := os.Getenv("MONGO_PREFIX")
	if prefix == "" {
		return nil, fmt.Errorf("MONGO_PREFIX environment variable not set")
	}

	client, err := database.GetClient()
	if err != nil {
		return nil, fmt.Errorf("failed to connect to database: %v", err)
	}

	databases, err := client.ListDatabaseNames(context.Background(), bson.D{})
	if err != nil {
		return nil, fmt.Errorf("failed to read databases: %v", err)
	}

	var projects []types.ProjectList
	for _, db := range databases {
		if strings.HasPrefix(db, prefix) {
			var settings struct {
				LastOpened time.Time `bson:"LastOpened"`
				CreatedAt  time.Time `bson:"CreatedAt"`
			}

			err = client.Database(db).Collection("settings").FindOne(context.TODO(), bson.D{}).Decode(&settings)
			if err != nil {
				log.Fatalf("Error fetching settings for database %s: %v", db, err)
				continue // Skip this database and proceed to the next
			}
			fmt.Println(settings.LastOpened)

			name := strings.Join(strings.Split(db, prefix+"-"), "")
			projects = append(projects, types.ProjectList{
				Name:       name,
				LastOpened: settings.LastOpened,
				CreatedAt:  settings.CreatedAt,
			})
		}
	}

	sort.Slice(projects, func(i, j int) bool {
		return projects[i].LastOpened.After(projects[j].LastOpened)
	})

	// Apply limit if specified
	if limit > 0 && len(projects) > limit {
		projects = projects[:limit]
	}

	return projects, nil
}
