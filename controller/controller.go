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
	// Landing page
	app.Get("/", func(c fiber.Ctx) error {
		project := model.Project{}
		result, err := project.GetAllProjects(5)
		if err != nil {
			// return Render(c, RenderLandingPage())
			log.Fatalf("Failed to get projects")
		}
		return utils.Render(c, views.LandingPage(result))
	})

	// Landing page
	app.Get("/projects", func(c fiber.Ctx) error {
		project := model.Project{}
		result, err := project.GetAllProjects(-1)
		if err != nil {
			// return Render(c, RenderLandingPage())
			log.Fatalf("Failed to get projects")
		}
		return utils.Render(c, views.ProjectsPage(result))
	})

	app.Delete("/project/:title", func(c fiber.Ctx) error {
		return nil
	})

	app.Get("/project/:title", func(c fiber.Ctx) error {
		return utils.Render(c, views.ProjectPage())
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
			LastOpened: time.Time{},
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
