package types

import "time"

type ProjectList struct {
	Name       string
	CreatedAt  time.Time
	LastOpened time.Time
}

type Color struct {
	R int `bson:"r"`
	G int `bson:"g"`
	B int `bson:"b"`
}

type Tag struct {
	Name  string
	Color Color
}
