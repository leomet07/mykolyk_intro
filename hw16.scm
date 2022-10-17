;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw16) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4 sec4
;Team name: Trees and trains
;HW16 -- Effecient quadsolve
;2022-10-16
;time cost: 0.25 (hours)

; Returns the discriminant of the quadratic equation represented by a,b,c
(define discriminant
  (lambda (a b c)
    (- (* b b) (* 4 a c))
    ))

; Gets the positive root of a quadratic equation
(define root1
  (lambda (a b c)
    (/
     (+
      (* -1 b)
      (sqrt (discriminant a b c))
     )
     (* 2 a)
    )))

; this function solves a quadratic
; first it checks if there are no real roots (if discriminant < 0) and it states that there are no real roots if so
; else, solve for the "plus version" root
(define quadSolve
  (lambda (a b c)
    (if
     (< (discriminant a b c) 0)
     "no real roots"
     (root1 a b c)
     )
   ))


(quadSolve 2 2 -4) "...should be 1"

(quadSolve 1 2 1) "...should be -1"

(quadSolve 1 1 4) "...should be no real roots"

(quadSolve -6 -3 6) "...should be #i-1.28..."

(quadSolve 2 3 1) "...should be -0.5"


