package main

import (
	"fmt"
	"net/http"
)

func requeda(w http.ResponseWriter, r *http.Request) {
	fmt.Println(w, "servidor inciado...")

}

func main() {
	http.HandleFunc("/", requeda)
	http.ListenAndServe(":8000", nil)

}
