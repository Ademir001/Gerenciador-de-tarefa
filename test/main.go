package main

import (
	"log"
	"net/http"
)

func main() {
	r := RegisterRouter()
	log.Println("Servidor")
	http.ListenAndServe(":8000", r)

}
