;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname lab1_draft) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define foo
  (lambda (n g)
     (/(+ g (/ n g)) 2)))

(sqrt 7) "...real ^^^"

(foo 9 2)
(foo 9 3)
(foo 9 4)