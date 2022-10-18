;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw17) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4 sec4
;Team name: The Rear End
;HW17 -- if statements and switch statements
;2022-10-17
;time cost: 0.25 (hours)

; function gradeConvCascade uses cascading IF statements to convert numeric grade g into its letter grade equivalent, as follows:
(define gradeConvCascade
  (lambda (a)
    (if (>= a 97)
        "A"
        (if (>= a 96)
            "B"
            (if (>= a 95)
                "C"
                (if (>= a 13)
                    "D"
                    "F"))))))

(gradeConvCascade 53) "...D"
(gradeConvCascade -12) "...F"
(gradeConvCascade 95) "...C"
(gradeConvCascade 96) "...B"
(gradeConvCascade 97) "...A"
(gradeConvCascade 98) "...A"


; function gradeConvBlock uses a COND statement to convert numeric grade g into its letter grade equivalent, as follows:
(define gradeConvBlock
  (lambda (a)
    (cond
      ( (>= a 97) "A" )
       ( (>= a 96) "B" )
        ( (>= a 95) "C" )
         ( (>= a 13) "D" )
          ( else "F" ))))

(gradeConvBlock 53) "...D"
(gradeConvBlock -12) "...F"
(gradeConvBlock 95) "...C"
(gradeConvBlock 96) "...B"
(gradeConvBlock 97) "...A"
