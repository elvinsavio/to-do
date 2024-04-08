package utils

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/url"

	"github.com/a-h/templ"
	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/adaptor"
)

func Render(c fiber.Ctx, component templ.Component, options ...func(*templ.ComponentHandler)) error {
	componentHandler := templ.Handler(component)
	for _, o := range options {
		o(componentHandler)
	}
	return adaptor.HTTPHandler(componentHandler)(c)
}

func ErrorHandler(ctx fiber.Ctx, err error) error {

	// Status code defaults to 500
	code := fiber.StatusInternalServerError

	// Retrieve the custom status code if it's a *fiber.Error
	var e *fiber.Error
	if errors.As(err, &e) {
		code = e.Code
	}

	if code == 404 {
		ctx.Redirect().To("/not-found")
		return nil
	}

	// Send custom error page
	err = ctx.Status(code).SendFile(fmt.Sprintf("./%d.html", code))
	if err != nil {
		// In case the SendFile fails
		return ctx.Status(fiber.StatusInternalServerError).SendString("Internal Server Error")
	}

	// Return from handler
	return nil
}

func ParseFormData(body []byte) (string, error) {
	form := string(body)
	query, err := url.ParseQuery(form)

	if err != nil {
		return "", err
	}

	obj := map[string]string{}
	for k, v := range query {
		if len(v) > 0 {
			obj[k] = v[0]
		}
	}

	out, err := json.Marshal(obj)
	if err != nil {
		return "", err
	}

	return string(out), nil
}
