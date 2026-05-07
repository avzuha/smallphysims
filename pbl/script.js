const e = 1.602e-19;
const c = 3e8;
const h_actual = 6.626e-34;

const ledData = {
  red: { lambda: 660e-9, color: "Red" },
  yellow: { lambda: 580e-9, color: "Yellow" },
  green: { lambda: 525e-9, color: "Green" },
  blue: { lambda: 450e-9, color: "Blue" }
};

let recordedValues = [];
let graphData = [];

function getThreshold(lambda) {
  return (h_actual * c) / (e * lambda);
}

function updateLED(color) {
  let v = parseFloat(document.getElementById(`volt-${color}`).value);
  document.getElementById(`val-${color}`).innerText = v.toFixed(2)+" V";

  if(v >= getThreshold(ledData[color].lambda))
    document.getElementById(`led-${color}`).classList.add("active");
  else
    document.getElementById(`led-${color}`).classList.remove("active");
}

["red","yellow","green","blue"].forEach(c=>{
  document.getElementById(`volt-${c}`)
    .addEventListener("input",()=>updateLED(c));
  updateLED(c);
});

function record(color){
  let v = parseFloat(document.getElementById(`volt-${color}`).value);
  let lambda = ledData[color].lambda;

  let h_calc = (e*lambda*v)/c;
  let freq = c/lambda;
  let energy = e*v;

  let row = document.getElementById("results-body").insertRow();
  row.innerHTML = `
    <td>${ledData[color].color}</td>
    <td>${(lambda*1e9).toFixed(0)}</td>
    <td>${v.toFixed(2)}</td>
    <td>${h_calc.toExponential(4)}</td>
  `;

  recordedValues.push(h_calc);
  graphData.push({freq, energy});

  let avg = recordedValues.reduce((a,b)=>a+b,0)/recordedValues.length;
  document.getElementById("avg-h").innerText =
    `Average Planck's Constant: ${avg.toExponential(4)} J·s`;
}

function plotGraph(){
  if(graphData.length<2){
    alert("Record at least 2 values!");
    return;
  }

  document.getElementById("graph-section").style.display="block";

  let x = graphData.map(d=>d.freq);
  let y = graphData.map(d=>d.energy);

  let n=x.length;
  let sumX=x.reduce((a,b)=>a+b,0);
  let sumY=y.reduce((a,b)=>a+b,0);
  let sumXY=x.reduce((s,xi,i)=>s+xi*y[i],0);
  let sumX2=x.reduce((s,xi)=>s+xi*xi,0);

  let slope=(n*sumXY - sumX*sumY)/(n*sumX2 - sumX*sumX);

  const canvas=document.getElementById("graphCanvas");
  const ctx=canvas.getContext("2d");
  ctx.clearRect(0,0,800,450);

  const margin=80, width=650, height=300;
  let maxX=Math.max(...x), maxY=Math.max(...y);

  // axes
  ctx.strokeStyle="white";
  ctx.beginPath();
  ctx.moveTo(margin,margin);
  ctx.lineTo(margin,margin+height);
  ctx.lineTo(margin+width,margin+height);
  ctx.stroke();

  // ticks
  let xTicks=5, yTicks=5;
  ctx.fillStyle="white";
  ctx.font="12px Arial";

  for(let i=0;i<=xTicks;i++){
    let val=(i/xTicks)*maxX;
    let px=margin+(i/xTicks)*width;
    ctx.beginPath();
    ctx.moveTo(px,margin+height);
    ctx.lineTo(px,margin+height+5);
    ctx.stroke();
    ctx.fillText(val.toExponential(1),px-25,margin+height+


        ctx.beginPath();
        ctx.arc(px,py,5,0,2*Math.PI);
        ctx.fill();
    });

    // line
    ctx.strokeStyle="yellow";
    ctx.beginPath();
    ctx.moveTo(margin,margin+height);
    ctx.lineTo(
        margin+width,
        margin+height-(slope*maxX/maxY)*height
    );
    ctx.stroke();

    document.getElementById("regression-result").innerText =
        `Regression h: ${slope.toExponential(4)} J·s`;

    let avg = recordedValues.reduce((a,b)=>a+b,0)/recordedValues.length;
    let error = Math.abs((slope-avg)/avg)*100;

    document.getElementById("error-result").innerText =
        `Percentage Error: ${error.toFixed(2)}%`;
}

</script>

</body>
</html>