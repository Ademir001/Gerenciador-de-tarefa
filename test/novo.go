package main

import (
	"fmt"
	"net/http"
)

// Rota: /
func homeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Servidor iniciado")
}

// Rota: /hello
func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Olá Mundo")
}

// Rota: /about
func aboutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Este é um servidor em Go")
}

func main() {
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/hello", helloHandler)
	http.HandleFunc("/about", aboutHandler)

	fmt.Println("Servidor iniciado em http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
