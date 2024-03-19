package controller

import (
	"context"
	database "elvinsavio/todo/database"
	"errors"
	"log"

	"go.mongodb.org/mongo-driver/bson"
)

func NewProject(projectName string) (bool, error) {
	client, err := database.GetClient()
	if err != nil {
		log.Fatal("Failed to connect to db")
	}
	exists, err := database.CheckIfDatabaseExists(client, projectName)

	if err != nil {
		log.Fatalf("Failed to check if DataBase Exists: " + err.Error())
		return false, errors.New("something went wrong")
	}

	if exists {
		return false, errors.New(projectName + " already exists")
	}

	client.Database(projectName).Collection("settings")

	settings := bson.D{{Key: "theme", Value: "dark"}}

	client.Database(projectName).Collection("settings").InsertOne(context.TODO(), settings)

	return true, nil
}
