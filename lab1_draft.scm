;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname lab1_draft) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define foo
  (lambda (n g)
     (/(+ g (/ n g)) 2)))

(foo 4 2) "...should be 2"
(foo 4 1) "...should be 2.5"
(foo 4 5) "...should be 2.9"
(foo 9 3) "...should be 3"
(foo 9 1) "...should be 5"
(foo 9 10) "...should be 5.45"
(foo 16 4) "...should be 4"
(foo 16 1) "...should be 8.5"
(foo 16 15) "...should be 8.03"
(foo 16 900) "...should be 450.008"
(foo 10 2) "...should be 3.5"
(foo 12 2) "...should be 4"

(define epsilon 0.1)

(define isGoodEnuf?
  (lambda (a b)
    (< (abs (- a b)) epsilon)))

(define mySqrtHelper
  (lambda (n g)
    (if (isGoodEnuf? n (* g g))
        g
        (mySqrtHelper n (foo n g) ))))

(define mySqrt
  (lambda (n)
    (mySqrtHelper n (/ n 3))))

(mySqrt 169) "...should be ~13"
(mySqrt 1234) "...should be ~35.1"
(mySqrt 4) "...should be ~2"
(mySqrt 16) "...should be ~4"
(mySqrt 144) "...should be ~12"