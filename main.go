package main

import (
	"log"

	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/template/html/v2"
)

func main() {
	engine := html.New("./templates/pages/", ".html")
	app := fiber.New(fiber.Config{
		Views: engine,
	})

	app.Static("/", "./static", fiber.Static{
		CacheDuration: 0,
	})

	// GET /api/register
	app.Get("/", func(c fiber.Ctx) error {
		return c.Render("landing", fiber.Map{}, "_base")
	})
	log.Fatal(app.Listen(":3000"))
}
