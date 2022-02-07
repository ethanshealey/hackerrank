const kidsWithCandies = (candies, extraCandies, res = []) => {
    candies.forEach((count, i) => Math.max(...candies, count + extraCandies) === count + extraCandies ? res.push(1) : res.push(0))
    return res
}
