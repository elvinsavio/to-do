package main

import (
	template "elvinsavio/todo/templates/pages/landing"
	types "elvinsavio/todo/types"

	"github.com/a-h/templ"
	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/log"
	"github.com/gofiber/fiber/v3/middleware/adaptor"
	"github.com/gofiber/fiber/v3/middleware/cache"
)

func main() {
	app := fiber.New()
	app.Static("/", "./static")

	app.Use(cache.New(cache.Config{
		CacheControl: true,
	}))

	app.Get("/", func(c fiber.Ctx) error {
		projects := []types.ProjectList{
			{
				Name:       "sample",
				Path:       "sample-project",
				LastOpened: "10-11-1998",
				Created:    "10-11-1998",
			},
			{
				Name:       "test project 2",
				Path:       "sample-project-2",
				LastOpened: "10-11-1998",
				Created:    "10-11-1998",
			},
			{
				Name:       "rip off google",
				Path:       "sample-rip-off",
				LastOpened: "10-11-1998",
				Created:    "10-11-1998",
			},
		}
		return Render(c, template.Landing(projects))
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
