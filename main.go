package main

import (
	"elvinsavio/todo/config"
	"elvinsavio/todo/controller"
	"elvinsavio/todo/database"
	"elvinsavio/todo/utils"

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

	app := fiber.New(fiber.Config{
		ErrorHandler: utils.ErrorHandler,
	})

	app.Static("/", "./views/static")

	app.Use(cache.New(cache.Config{
		CacheControl: false,
		Next: func(c fiber.Ctx) bool {
			return c.Query("noCache") == "true"
		},
	}))

	app = controller.New(app)

	log.Fatal(app.Listen(":3000"))
}
