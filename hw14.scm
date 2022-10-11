;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw14) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Divide by 10 because floor only removes things after the decimal point
(define getOnesDigit
  (lambda (a)
    (floor
     (*
      (-
       (/ a 10)
       (floor (/ a 10))
      )
      10
      ))))
    

(getOnesDigit 124)
"...should be 4"

(getOnesDigit 5)
"...should be 5"

(getOnesDigit 212137.124)
"...should be 7"

(getOnesDigit -4914927285)
"...should be 5"

; Returns the discriminant of the quadratic equation represented by a,b,c
(define discriminant
  (lambda (a b c)
    (- (* b b) (* 4 a c))
    ))

(discriminant 4 2 2)
"...should be -28"

(discriminant 2 4 2)
"...should be 0"

(discriminant 5 10 3)
"...should be 40"

(discriminant 3 8 7)
"...should be -20"

; Gets the positive root of a quadratic equation
(define root1
  (lambda (a b c)
    (/ (+ (* -1 b) (sqrt (discriminant a b c ))) (* 2 a))))

(root1 2 4 2)
"...should be -1"

(root1 4 8 12)
"...should be -1.0+1.4142..."

(root1 1 5 6)
"...should be -2"

(define getHundredsDigit
  (lambda (a)
    (floor
     (*
      (-
       (/ a 1000)
       (floor (/ a 1000))
      )
      10
      ))))

(getHundredsDigit 234)
"...should be 2"

(getHundredsDigit 76348)
"...should be 3"

(getHundredsDigit 890732)
"...should be 7"

(getHundredsDigit 3)
"...should be 0"

(define disaster
  (lambda (a b c)
    (/ c (+ a b))
    ))

(disaster 20 80 100)
"...should be 1"

(disaster 4 2 30)
"...should be 5"

(disaster 8 2 30)
"...should be 3"

(disaster 8 2 88)
"...should be 8.8"