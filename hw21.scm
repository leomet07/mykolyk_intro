;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw21) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;IntroCS pd4 sec4
;Team name: The Rear End
;collaborated with team
;HW22 -- Idiomatic Construction -- sumOdd, numDigits, sumOddDigits
;2022-10-25
;time cost: 1.2 (hours)

; returns bool value if n is even
(define isEven
  (lambda (n)
    (=(remainder (floor n) 2) 0)))


; the function sumPtoQ takes inputs p and q returns the sum of the integers from p to q, inclusive.
(define sumPtoQ
  (lambda (p q)
    (if (< p q)
        (+ p (sumPtoQ (+ p 2) q))
        q
        )))

; (sumOdd n) takes non-negative integer n, and returns the sum of the positive odd integers up to and including n.
(define sumOdd
  (lambda (n)
    (if (= n 0)
        0
        (if (isEven n)
            (sumOdd (- n 1))
            (sumPtoQ 1 n)
            )
        )
    ))

(sumOdd 0) "...should be 0"
(sumOdd 1) "...should be 1"
(sumOdd 2) "...should be 1"
(sumOdd 3) "...should be 4"
(sumOdd 9) "...should be 25"
(sumOdd 10) "...should be 25"
(sumOdd 11) "...should be 36"
(sumOdd 12) "...should be 36"


; the function numDigits takes positive integer n and returns the number of digits in n.
(define numDigits
  (lambda (n)
    (if (< (/ n 10) 1)
        1
        (+ 1 (numDigits (/ n 10))))))

(numDigits 5) "...should be 1"
(numDigits 35) "...should be 2"
(numDigits 492067) "...should be 6"
(numDigits 4) "...should be 1"
(numDigits 45) "...should be 2"
(numDigits 87652)  "...should be 5"
(numDigits 10) "...should be 2"

(define sumOddDigits
  (lambda (n)
    (if(< n 10)
       (if(= (remainder n 2) 1)
          n
          0)
       (if(= (remainder (remainder n 10) 2) 1)
          (+ (remainder n 10) (sumOddDigits (quotient n 10)))
          (sumOddDigits(quotient n 10))))))

(sumOddDigits 0) "...should be 0"
(sumOddDigits 4) "...should be 0"
(sumOddDigits 3) "...should be 3"
(sumOddDigits 27) "...should be 7"
(sumOddDigits 1984) "...should be 10"
(sumOddDigits 492067) "...should be 16"
(sumOddDigits 69) "...should be 9"
(sumOddDigits 420) "...should be 0"
(sumOddDigits 62122159) "...should be 16"