package main

import (
	"fmt"
	"net/http"
)

func homehandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Bem-vindo"))
}

func saudacaohandler(w http.ResponseWriter, r *http.Request) {
	vars := max.vars(r)
	nome := vars["nome"]
	msg := fmt.Sprintf("ola,%s!", nome)
	w.Write([]byte(msg))
}
func somahandler(w http.ResponseWriter, r *http.Request) {
	aStr := r.URL.Query().Get("a")
}

func main() {

}
