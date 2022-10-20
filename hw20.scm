;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw20) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;IntroCS pd4 sec4
;Team name: The Rear End
;collaborated with team
;HW20 -- Bigger Steps, Different Domain
;2022-10-20
;time cost: 0.5 (hours)

; the function fiction takes inputs n and accomplishes a task similar to that of fact, but only includes every 3rd integer in the final product.
(define fiction
  (lambda (n)
    (if (> n 1)
        (* n (fiction (- n 3)))
        1
        )))

(fiction 0) "...should be 1"
(fiction 1) "...should be 1"
(fiction 2) "...should be 2"
(fiction 3) "...should be 3"
(fiction 4) "...should be 4"
(fiction 5) "...should be 10"
(fiction 6) "...should be 18"
(fiction 7) "...should be 28"
(fiction 8) "...should be 80"
(fiction 9) "...should be 162"

; the function sumPtoQ takes inputs p and q returns the sum of the integers from p to q, inclusive.
(define sumPtoQ
  (lambda (p q)
    (if (< p q)
     (+ p (sumPtoQ (+ p 1) q))
     q
     )))

(sumPtoQ 0 0) "...should be 0"
(sumPtoQ 0 3) "...should be 6"
(sumPtoQ 2 3) "...should be 5"
(sumPtoQ 3 3) "...should be 3"
(sumPtoQ 6 7) "...should be 13"
(sumPtoQ 7 9) "...should be 24"
