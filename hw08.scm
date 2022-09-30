;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw08) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4
;HW08 -- Spoken Word to Coded Form, or in my words, implementing simple mathmatical functions.
;2022-09-29
;time cost: 1.1 (hours)


; PLAIN ENGLISH DEFINITION: The ArithMean3 function will add its first input, a, to its second input b.
; Then, it will add its third input to their sum. Next, this sum will be divided by the number of inputs, 3.
(define ArithMean3 (lambda (a b c) (/ (+ a b c) 3) ) )

(ArithMean3 0 0 0)
"...should be 0"

(ArithMean3 1 2 3)
"...should be 2"

(ArithMean3 5 -10 20)
"...should be 5"

; The GetReciprocal function is a HELPER FUNCTION that acts as a "reciprocal" operator and helps me write DRY code.
(define GetReciprocal (lambda (n) (/ 1 n) ))

; PLAIN ENGLISH DEFINITION: The HarMean3 will get the arithmetic mean (via the ArithMean3 function) of each of the reciprocals of the three inputs.
; Next, it will return the reciprocal of the result of the arithmetic mean.
(define HarMean3 (lambda (a b c) (GetReciprocal (ArithMean3 (GetReciprocal a) (GetReciprocal b) (GetReciprocal c) )) ) )

(HarMean3 5 5 5)
"...should be 5"

(HarMean3 3 6 18)
"...should be 5.4"

(HarMean3 5 -10 20)
"...should be 20"

; The GetOneDimensionalDistance function is a HELPER FUNCTION that simplifies getting the distance between two points on the same axis and helps me write DRY code.
(define GetOneDimensionalDistance (lambda (a b) (abs (- a b))) )

; PLAIN ENGLISH DEFINITION: The CartDist function gets the Euclidean distance between two points.
; It squares each of the differences between 2 X coords and 2 Y coords (each from a diff point), and then adds them. The square root of the sum is the output, the Euclidean distance.
(define CartDist (lambda (X1 Y1 X2 Y2) (sqrt (+ (expt (GetOneDimensionalDistance X1 X2) 2) (expt (GetOneDimensionalDistance Y1 Y2) 2)) ) ))

(CartDist 0 0 0 0)
"...should be 0"

(CartDist 4 4 4 4)
"...should be 0"

(CartDist 0 0 3 4)
"...should be 5"

; CHALLENGE
; The MAX2 function is a MAX function implementation with only math and simple operators.
; It gets the distance between A and B, and adds it to the sum of A and B.
; The distance being added brings the smaller (lesser) term up to the larger one, so the sum is twice the larger input.
; Then to find the larger input, you simply divide by 2. The quotient is the larger number, which is what the max/MAX2 function should return.
(define MAX2 (lambda (a b) (/ (+ (+ a b) (abs (- a b))) 2) ))

(MAX2 4 4)
"... should be 4"

(MAX2 4 7)
"... should be 7"

(MAX2 9 8)
"... should be 9"

