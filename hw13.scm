;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw13) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4 secX
;Team name: Trees and trains
;HW13 -- Pythagorean Triples
;2022-10-07
;time cost: 0.5 (hours)
;collaborated with: Jia L

; This function returns true only if the inputs a and b are valid legs of a right triangle and if C is the valid hypotenuse for that right triangle
(define isPythTriple_helper
  (lambda (a b c)
    (=
     (* c c)
     (+ (* b b) (* a a))
     )))

; The isPythTriple? function returns true if any of its inputs are valid legs and hypotenuses for a right triangle
(define isPythTriple?
  (lambda (a b c)
    (or
     (isPythTriple_helper a b c)
     (isPythTriple_helper c b a)
     (isPythTriple_helper c a b)
     )))

(isPythTriple? 3 4 5)
"...should be t"

(isPythTriple? 3 4 6)
"...should be f"

(isPythTriple? 5 12 13)
"...should be t"

(isPythTriple? 20 21 29)
"...should be t"

(isPythTriple? 9 40 41)
"...should be t"

(isPythTriple? 41 40 9)
"...should be t"

(isPythTriple? 41 40 8)
"...should be f"

(isPythTriple? 8 10 6)
"...should be t"
