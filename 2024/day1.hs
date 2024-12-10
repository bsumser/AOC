import System.IO
import Text.Read (readMaybe)
import Data.List (splitAt)

main :: IO ()
main = do
  contents <- readFile "day1.txt"
  let linesList = lines contents
  let parsedPairs = map parseInts linesList
  case sequence parsedPairs of
    Just nums -> do
      let (list1, list2) = unzip nums
      print list1  -- First column
      print list2  -- Second column
    Nothing -> putStrLn "Error: Could not parse numbers"

parseInts :: String -> Maybe (Integer, Integer)
parseInts line = do
  let [a, b] = words line  -- Split the line into words (strings)
  x <- readMaybe a
  y <- readMaybe b
  return (x, y)
