package config

import (
	"log"
	"os"

	"github.com/pelletier/go-toml"
)

func LoadEnv() {
	config, err := toml.LoadFile("config.toml")
	if err != nil {
		log.Fatalf("Error loading TOML file: %s", err)
	}

	log.Println("Loading env files")

	// Iterate over the keys and set environment variables
	for key, value := range config.ToMap() {
		// Convert value to string
		strValue, ok := value.(string)
		if !ok {
			log.Printf("Error converting value to string for key: %s", key)
			continue
		}

		// Set the environment variable
		os.Setenv(key, strValue)
	}
}
