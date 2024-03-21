package database

import (
	"context"
	"fmt"
	"log"
	"os"
	"sync"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var (
	client *mongo.Client
	once   sync.Once
)

// Connect initializes a connection to MongoDB
func New() (*mongo.Client, error) {
	var err error
	once.Do(func() {
		uri := os.Getenv("MONGO_URI")
		if uri == "" {
			log.Fatalf("MONGO_URI not set.")
		}
		client, err = mongo.Connect(context.TODO(), options.Client().ApplyURI(uri))
		if err != nil {
			log.Fatalf("Failed to connect to mongo.")
		}
	})
	return client, err
}

// GetClient returns the MongoDB client
func GetClient() (*mongo.Client, error) {
	if client == nil {
		return nil, fmt.Errorf("MongoDB client is not initialized")
	}
	return client, nil
}

// Disconnect closes the connection to MongoDB
func Disconnect() error {
	if client == nil {
		return fmt.Errorf("MongoDB client is not initialized")
	}
	if err := client.Disconnect(context.TODO()); err != nil {
		return err
	}
	return nil
}
