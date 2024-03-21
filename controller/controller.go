package controller

import (
	model "elvinsavio/todo/model"
	LandingPage "elvinsavio/todo/views/pages/landing"
	NewProjectPage "elvinsavio/todo/views/pages/new"

	"elvinsavio/todo/utils"

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
		return utils.Render(c, LandingPage.Render(result))
	})

	// New project page
	app.Get("/new", func(c fiber.Ctx) error {
		return utils.Render(c, NewProjectPage.Render(""))
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
			return utils.Render(c, NewProjectPage.Render(err.Error()))
		}

		return c.Redirect().To("/project/" + projectName)
	})

	return app
}
