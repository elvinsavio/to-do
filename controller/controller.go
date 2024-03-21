package controller

import (
	model "elvinsavio/todo/model"
	"log"
	"strings"
	"time"

	"github.com/a-h/templ"
	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/adaptor"
)

func New(app *fiber.App) *fiber.App {

	// Landing page
	app.Get("/", func(c fiber.Ctx) error {
		project := model.Project{}
		result, err := project.GetAllProjects()
		if err != nil {
			// return Render(c, RenderLandingPage())
			log.Fatalf("Failed to get projects")
		}
		return Render(c, RenderLandingPage(result))
	})

	// New project page
	app.Get("/new", func(c fiber.Ctx) error {
		return Render(c, RenderNewPage(""))
	})

	app.Post("/new", func(c fiber.Ctx) error {
		projectName := c.FormValue("name")
		projectName = strings.Trim(projectName, " ")
		projectName = strings.ReplaceAll(projectName, " ", "-")

		project := model.Project{
			Name:       projectName,
			Theme:      "dark",
			CreatedAt:  time.Now(),
			LastOpened: nil,
		}

		_, err := project.NewProject()
		if err != nil {
			return Render(c, RenderNewPage(err.Error()))
		}

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
