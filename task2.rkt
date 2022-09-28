;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname task2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Name: Lenny Metlitsky
; Date: 9/23/22
; Team name: Trees and trains
; Period: 4
; Roster: Leonid Metlitsky (232884742)

; Basically, the DrRacket stepper runs each line on its own, step by step.
; It prints the output of each line.
; It's the built-in debugger.

; Simply return the argument back
; SHORTHAND: (define (foo d) d)
(define foo (lambda (d) d))

(foo 1)
(foo 0)
(foo 10)


; ALWAYS returns area of a circle with the radius of 1
(define areaCirc (lambda (R) (* 1 pi) ) )

(areaCirc 1)
(areaCirc 3)
(areaCirc 5)

; Return the area of the circle with the radius that is passed in via the function argument

(define AreaCirc (lambda (R) ( * (* (expt R 2) pi) ))  ) )

(AreaCirc 1)
(AreaCirc 3)
(AreaCirc 5)

; HOMEWORK: Write a Prodecure and give it a name
(define (getRadius area) (sqrt (/ area pi)) )

; Should be approx 3, prints 3
(getRadius 28.274333882308138)

; Should be approx 8, prints 8
(getRadius 201.06192982974676)
