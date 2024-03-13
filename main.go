package main

import (
	template "elvinsavio/todo/templates/pages/landing"

	"github.com/a-h/templ"
	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/log"
	"github.com/gofiber/fiber/v3/middleware/adaptor"
)

func main() {
	app := fiber.New()
	app.Static("/", "./static")
	app.Get("/", func(c fiber.Ctx) error {

		return Render(c, template.Landing())
	})

	log.Fatal(app.Listen(":3000"))
}

func Render(c fiber.Ctx, component templ.Component, options ...func(*templ.ComponentHandler)) error {
	componentHandler := templ.Handler(component)
	for _, o := range options {
		o(componentHandler)
	}
	return adaptor.HTTPHandler(componentHandler)(c)
}
