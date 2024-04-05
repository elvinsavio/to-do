package model

import (
	"context"
	"elvinsavio/todo/database"
	"elvinsavio/todo/types"
	"fmt"
	"os"

	"go.mongodb.org/mongo-driver/bson"
)

func GetAllTags(projectName string) ([]types.Tag, error) {
	prefix := os.Getenv("MONGO_PREFIX")
	if prefix == "" {
		return nil, fmt.Errorf("MONGO_PREFIX not set")
	}

	projectName = prefix + "-" + projectName

	client, err := database.GetClient()
	if err != nil {
		return nil, fmt.Errorf("failed to connect to db: %v", err.Error())
	}

	collection := client.Database(projectName).Collection("tags")
	cursor, err := collection.Find(context.TODO(), bson.D{})
	if err != nil {
		return nil, fmt.Errorf("failed to retrieve data: %v", err)
	}

	// decode the result
	var tags []types.Tag
	if err = cursor.All(context.TODO(), &tags); err != nil {
		panic(err)
	}
	return tags, nil
}
