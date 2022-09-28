;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname task3) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Name: Lenny Metlitsky
; Partner: Jia Lin
; Date: 9/28/22
; Team name: Trees and trains
; Period: 4
; Roster: Leonid Metlitsky (232884742)


; Simply return the argument back
; SHORTHAND: (define (foo d) d)
(define foo (lambda (d) d))

(foo 1)
"...should be 1"

(foo 0)
"...should be 0"

(foo 10)
"...should be 10"


; ALWAYS returns area of a circle with the radius of 1.
(define areaCirc (lambda (R) (* 1 pi) ) )

(areaCirc 1)
"...should be #i3.141592653589793"

(areaCirc 3)
"...should be #i3.141592653589793"

(areaCirc 5)
"...should be #i3.141592653589793"


; Return the area of the circle with the radius that is passed in via the function argument.
(define AreaCirc (lambda (R) (* (expt R 2) pi) )  ) 

(AreaCirc 1)
"...should be #i3.141592653589793"

(AreaCirc 3)
"...should be #i28.274333882308138"

(AreaCirc 5)
"...should be #i78.53981633974483"


; My definition of a washer: A large circle with a smaller circle cut out in the direct center.
; AreaWasher gets the area of a washer, with the arguments of the radius of the outer and inner circles.
; NOTE: The order that the radii are passed in does NOT matter, as the absolute value of the difference of the two areas is used.
(define AreaWasher (lambda (r1 r2) (abs (- (AreaCirc r1) (AreaCirc r2) ))) )

(AreaWasher 3 1)
"...should be #i25.132741228718345"

(AreaWasher 1 3)
"...should be #i25.132741228718345"
