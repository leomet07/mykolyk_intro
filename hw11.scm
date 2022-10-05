;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw11) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4 secX
;HW11 --  Seeking Truth, XOR + Bidirectional IF
;2022-10-05
;time cost: 0.5 (hours)
;collaborated with: Jia L, Eli L

; XOR, this function takes two booleans, a and b, and returns true if only one is true, otherwise returns false
(define XOR
  (lambda (a b)
    (and
     (or a b)
     (or (not a) (not b) )
     )))

(XOR #t #t) "...should be #f"

(XOR #t #f) "...should be #t"

(XOR #f #t) "...should be #t"

(XOR #f #f) "...should be #f"

; Bidirectional IF, this function takes two booleans, a and b, and returns true if only both are true, otherwise returns false
(define bic
  (lambda (a b)
    (or
     (and a b)
     (and (not a) (not b) )
     )))

(bic #t #t) "...should be #t"

(bic #t #f) "...should be #f"

(bic #f #t) "...should be #f"

(bic #f #f) "...should be #t"

; XOR with 3 values, this function takes three booleans, a and b and c, and returns true if only one of them is true, otherwise returns false
(define XOR3
  (lambda (a b c)
    (and
     (or a b c)
     (or (not a) (not b))
     (or (not b) (not c))
     (or (not a) (not c))
     )))

(XOR3 #t #t #t) "...should be #f"

(XOR3 #t #t #f) "...should be #f"

(XOR3 #t #f #t)"...should be #f"

(XOR3 #t #f #f) "...should be #t"

(XOR3 #f #t #t) "...should be #f"

(XOR3 #f #t #f) "...should be #t"

(XOR3 #f #f #t) "...should be #t"

(XOR3 #f #f #f) "...should be #f"