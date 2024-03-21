package main

import (
	"elvinsavio/todo/config"
	"elvinsavio/todo/controller"
	"elvinsavio/todo/database"

	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/log"
	"github.com/gofiber/fiber/v3/middleware/cache"
)

func main() {
	config.LoadEnv()

	_, err := database.New()
	if err != nil {
		log.Fatalf("Failed to connect to Database", err)
	}

	app := fiber.New()
	app.Static("/", "./views/static")

	app = controller.New(app)

	app.Use(cache.New(cache.Config{
		CacheControl: false,
		Next: func(c fiber.Ctx) bool {
			return c.Query("noCache") == "true"
		},
	}))

	log.Fatal(app.Listen(":3000"))
}
