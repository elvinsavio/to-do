package controller

import (
	"fmt"
	"strings"

	"github.com/a-h/templ"
	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/adaptor"
)

func New(app *fiber.App) *fiber.App {

	// Landing page
	app.Get("/", func(c fiber.Ctx) error {
		return Render(c, RenderLandingPage())
	})

	// New project page
	app.Get("/new", func(c fiber.Ctx) error {
		fmt.Println("hello world")
		return Render(c, RenderNewPage())
	})

	app.Post("/new", func(c fiber.Ctx) error {
		projectName := c.FormValue("name")
		projectName = strings.Trim(projectName, " ")
		projectName = strings.ReplaceAll(projectName, " ", "-")
		fmt.Println("Project Name:", projectName)
		return c.Redirect().To("/project/" + projectName)
	})

	return app
}

func Render(c fiber.Ctx, component templ.Component, options ...func(*templ.ComponentHandler)) error {
	componentHandler := templ.Handler(component)
	for _, o := range options {
		o(componentHandler)
	}
	return adaptor.HTTPHandler(componentHandler)(c)
}
