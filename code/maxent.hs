

type ProbabilityDistribution = [Double]

-- The function x*log(x)
xlogx :: Double -> Double
xlogx x
    | x == 0.0 = 0.0
    | x >= 0.0 = x * (log x)
    | otherwise = undefined

-- The function x*log(x/y)
xlogxy :: (Double, Double) -> Double
xlogxy (x, y)
    | x == 0.0 = 0.0
    | x >= 0.0 = x * (log (x/y))
    | otherwise = undefined

-- Uniform distribution over n possibilities
uniform :: Int -> ProbabilityDistribution
uniform n = replicate n (1.0/(fromIntegral n))

-- Entropy of a probability distribution
entropy :: ProbabilityDistribution -> Double
entropy p = -sum (map xlogx p)

-- Kullback Leibler divergence
kl :: ProbabilityDistribution -> ProbabilityDistribution -> Double
kl p q = sum (map xlogxy (zip p q))

main = do
    let q = uniform 5
    let p = uniform 5
    print (kl p q)


