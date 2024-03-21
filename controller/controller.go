package controller

import (
	model "elvinsavio/todo/model"
	"elvinsavio/todo/utils"
	views "elvinsavio/todo/views/pages"

	"log"
	"strings"
	"time"

	"github.com/gofiber/fiber/v3"
)

func New(app *fiber.App) *fiber.App {
	// middle ware

	// Landing page
	app.Get("/", func(c fiber.Ctx) error {
		project := model.Project{}
		result, err := project.GetAllProjects()
		if err != nil {
			// return Render(c, RenderLandingPage())
			log.Fatalf("Failed to get projects")
		}
		return utils.Render(c, views.LandingPage(result))
	})

	// New project page
	app.Get("/new", func(c fiber.Ctx) error {
		return utils.Render(c, views.NewPage(""))
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
			return utils.Render(c, views.NewPage(err.Error()))
		}

		return c.Redirect().To("/project/" + projectName)
	})

	app.Get("/not-found", func(c fiber.Ctx) error {
		return utils.Render(c, views.NotFoundPage())
	})

	return app
}
