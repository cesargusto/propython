;; The first three lines of this file were inserted by DrScheme. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(planet plai/plai:1:3/lang/reader)
(test-inexact-epsilon 0.0001)

(define (somatoria termo a proximo b)
  (if (> a b)
      0
      (+ (termo a)
         (somatoria termo (proximo a) proximo b))))

(define (inc n) (+ 1 n))

(define (cubo n) (* n n n))

(define (soma-cubos a b)
  (somatoria cubo a inc b))

(test (soma-cubos 1 10) 3025)

(define (soma-ints a b)
  (somatoria (lambda (x) x) a inc b))

(test (soma-ints 1 10) 55)

(define (dicotomia-de-zeno a b)
  (define (termo-zeno n) (/ 1.0 (expt 2.0 n)))
  (somatoria termo-zeno a inc b))

(test (dicotomia-de-zeno 1 100) 1)

(define (soma-pi a b)
  (define (termo-pi x)
    (/ 1.0 (* x (+ x 2))))
  (define (prox-pi x)
    (+ x 4))
  (somatoria termo-pi a prox-pi b))

(test (* 8 (soma-pi 1 100000)) pi)

(define (integral f a b dx)
  (define (+dx x) (+ x dx))
  (* (somatoria f (+ a (/ dx 2.0)) +dx b) dx))
    
(test (integral cubo 0 1 0.01) .25)
