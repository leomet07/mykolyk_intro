;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw19) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4 sec4
;Team name: The Rear End
;HW18 -- factorial and recursion!
;2022-10-19
;time cost: 0.15 (hours)

; the function fact takes integer input n returns the value of n-factorial ( n! ).
; this function is an example of a recursive function.
; it takes the fact (factorial) of every number before n and then multiples n by that
(define fact
  (lambda (n)
    (if (> n 1)
     (* n (fact (- n 1)))
     1
     )))


(fact 0) "...should be 1"

(fact 1) "...should be 1"

(fact 2) "...should be 2"

(fact 3) "...should be 6"

(fact 4) "...should be 24"

(fact 5) "...should be 120"

(fact 6) "...should be 720"

(fact 7) "...should be 5040"

(fact 8) "...should be 40320"