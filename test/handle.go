package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

func RegisterRouter() *mux.Router {
	r := mux.NewRouter()
	r.HandleFunc("/hola", HolaHandle)
	return r
}

func HolaHandle(w http.ResponseWriter, r *http.Request) {
	fmt.Println(w, "pong")
}
