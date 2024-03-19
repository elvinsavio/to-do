package controller

import (
	"elvinsavio/todo/types"
	LandingPage "elvinsavio/todo/views/pages/landing"
	NewProjectPage "elvinsavio/todo/views/pages/new"

	"github.com/a-h/templ"
)

func RenderLandingPage() templ.Component {
	projects := []types.ProjectList{}
	return LandingPage.Render(projects)
}

func RenderNewPage(err string) templ.Component {
	return NewProjectPage.Render(err)
}
