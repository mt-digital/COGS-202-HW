;; Trying to copy the backprop example script backprop_cars.bsh from 
;; the simbrain example scripts (

(import '(org.simbrain.network NetworkComponent)
        '(org.simbrain.network.subnetworks BackpropNetwork)        
        '(org.simbrain.network.trainers BackpropTrainer)
        '(org.simbrain.util Utils)        
)


(def nwComp (NetworkComponent. "Backprop Cars"))

(def network (.getNetwork nwComp))

(def bp (BackpropNetwork. network (int-array [5 8 5])))

(.addGroup network bp)

(def training-set (.getTrainingSet bp))

(def input-file (clojure.java.io/file "input.csv"))
(def target-file (clojure.java.io/file "target.csv"))

(def input-mat (Utils/getDoubleMatrix input-file))
(def target-mat (Utils/getDoubleMatrix target-file))

(.setInputData training-set input-mat)
(.setTargetData training-set target-mat)

(def trainer (BackpropTrainer. bp (.getNeuronGroupsAsList bp)))
(.randomize trainer)
(def numiter 50)

(doseq [a (range numiter)]
  (.iterate trainer)
)

(defn format-output [output-vec]
  (clojure.string/join [
    "[" (clojure.string/join ", " 
          (map (fn [a] (format "%.3f" a)) output-vec)
        )
     "]"
    ]
  )
)

(defn show-output [input-vec]

  (let [il (.getInputLayer bp)]
    (.forceSetActivations il input-vec)
  )
  (.update bp)

  (let [ol (.getOutputLayer bp)]
    (def activation (.getActivations ol))
  )

  ; (println (java.util.Arrays/toString activation))
  (println (format-output activation))
)

(println "-------OUTPUTS--------")
(doseq [input-vec [
    (double-array [1 0 0 0 0])
    (double-array [0 1 0 0 0])
    (double-array [0 0 1 0 0])
    (double-array [0 0 0 1 0])
    (double-array [0 0 0 0 1])
    ]
  ]
  (println 
    (clojure.string/join ["\ntransition probabilities for " 
                          (java.util.Arrays/toString input-vec)
                         ]
    )
  )
  (show-output input-vec)
)

(println "-------EXPECTED-------")
(println "[0.00, 0.50, 0.20, 0.10, 0.20]")
(println "[0.00, 0.00, 0.70, 0.00, 0.30]")
(println "[0.10, 0.20, 0.30, 0.40, 0.00]")
(println "[0.60, 0.10, 0.10, 0.10, 0.10]")
(println "[0.00, 0.40, 0.00, 0.60, 0.00]")
