package database

import (
	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func CheckIfDatabaseExists(client *mongo.Client, databaseName string) (bool, error) {
	databases, err := client.ListDatabaseNames(context.Background(), bson.D{{}})
	if err != nil {
		return false, fmt.Errorf("failed to list database names: %v", err)

	}

	for _, db := range databases {
		if db == databaseName {
			return true, nil
		}
	}

	return false, nil
}
