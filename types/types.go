package types

import "time"

type ProjectList struct {
	Name       string
	CreatedAt  time.Time
	LastOpened time.Time
}
