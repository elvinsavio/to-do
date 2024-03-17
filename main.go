package main

import (
	"elvinsavio/todo/config"
	"elvinsavio/todo/controller"

	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/log"
	"github.com/gofiber/fiber/v3/middleware/cache"
)

func main() {
	config.LoadEnv()

	app := fiber.New()
	app.Static("/", "./views/static")

	app = controller.New(app)

	app.Use(cache.New(cache.Config{
		CacheControl: true,
	}))

	log.Fatal(app.Listen(":3000"))
}
