console.log("JS is running")

async function main() {
  await new Promise(r => setTimeout(r, 1000))
  console.log("done")
}

main()
