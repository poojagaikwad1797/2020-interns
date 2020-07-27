      function LineChart(con) {
        // user defined properties
        this.canvas = document.getElementById(con.canvasId);
        this.minX = con.minX;
        this.minY = con.minY;
        this.maxX = con.maxX;
        this.maxY = con.maxY;
        this.unitsPerTickX = con.unitsPerTickX;
        this.unitsPerTickY = con.unitsPerTickY;

        // constants
        this.padding = 10;
        this.tickSize = 10;
        this.axisColor = "#555";
        this.pointRadius = 5;
        this.font = "12pt Calibri";

        this.fontHeight = 12;

        // relationships
        this.context = this.canvas.getContext("2d");
        this.rangeX = this.maxX - this.minY;
        this.rangeY = this.maxY - this.minY;
        this.numXTicks = Math.round(this.rangeX / this.unitsPerTickX);
        this.numYTicks = Math.round(this.rangeY / this.unitsPerTickY);
        this.x = this.getLongestValueWidth() + this.padding * 2;
        this.y = this.padding * 2;
        this.width = this.canvas.width - this.x - this.padding * 2;
        this.height =
          this.canvas.height - this.y - this.padding - this.fontHeight;
        this.scaleX = this.width / this.rangeX;
        this.scaleY = this.height / this.rangeY;

        // draw x y axis and tick marks
        this.drawXAxis();
        this.drawYAxis();
      }

      LineChart.prototype.getLongestValueWidth = function () {
        this.context.font = this.font;
        var longestValueWidth = 0;
        for (var n = 0; n <= this.numYTicks; n++) {
          var value = this.maxY - n * this.unitsPerTickY;
          longestValueWidth = Math.max(
            longestValueWidth,
            this.context.measureText(value).width
          );
        }
        return longestValueWidth;
      };

      LineChart.prototype.drawXAxis = function () {
        var context = this.context;
        context.save();
        context.beginPath();
        context.moveTo(this.x, this.y + this.height);
        context.lineTo(this.x + this.width, this.y + this.height);
        context.strokeStyle = this.axisColor;
        context.lineWidth = 2;
        context.stroke();

        // draw tick marks
        for (var n = 0; n < this.numXTicks; n++) {
          context.beginPath();
          context.moveTo(
            ((n + 1) * this.width) / this.numXTicks + this.x,
            this.y + this.height
          );
          context.lineTo(
            ((n + 1) * this.width) / this.numXTicks + this.x,
            this.y + this.height - this.tickSize
          );
          context.stroke();
        }

        // draw labels
        context.font = this.font;
        context.fillStyle = "black";
        context.textAlign = "center";
        context.textBaseline = "middle";

        for (var n = 0; n < this.numXTicks; n++) {
          var label = Math.round(((n + 1) * this.maxX) / this.numXTicks);
          context.save();
          context.translate(
            ((n + 1) * this.width) / this.numXTicks + this.x,
            this.y + this.height + this.padding
          );
          context.fillText(label, 0, 0);
          context.restore();
        }
        context.restore();
      };

      LineChart.prototype.drawYAxis = function () {
        var context = this.context;
        context.save();
        context.save();
        context.beginPath();
        context.moveTo(this.x, this.y);
        context.lineTo(this.x, this.y + this.height);
        context.strokeStyle = this.axisColor;
        context.lineWidth = 2;
        context.stroke();
        context.restore();

        // draw tick marks
        for (var n = 0; n < this.numYTicks; n++) {
          context.beginPath();
          context.moveTo(this.x, (n * this.height) / this.numYTicks + this.y);
          context.lineTo(
            this.x + this.tickSize,
            (n * this.height) / this.numYTicks + this.y
          );
          context.stroke();
        }

        // draw values
        context.font = this.font;
        context.fillStyle = "black";
        context.textAlign = "right";
        context.textBaseline = "middle";

        for (var n = 0; n < this.numYTicks; n++) {
          var value = Math.round(this.maxY - (n * this.maxY) / this.numYTicks);
          context.save();
          context.translate(
            this.x - this.padding,
            (n * this.height) / this.numYTicks + this.y
          );
          context.fillText(value, 0, 0);
          context.restore();
        }
        context.restore();
      };

      LineChart.prototype.drawLine = function (data, color, width) {
        var context = this.context;
        context.save();
        this.transformContext();
        context.lineWidth = width;
        context.strokeStyle = color;
        context.fillStyle = color;
        context.beginPath();
        context.moveTo(data[0].x * this.scaleX, data[0].y * this.scaleY);

        for (var n = 0; n < data.length; n++) {
          var point = data[n];

          // draw segment
          context.lineTo(point.x * this.scaleX, point.y * this.scaleY);
          context.stroke();
          context.closePath();
          context.beginPath();
          context.arc(
            point.x * this.scaleX,
            point.y * this.scaleY,
            this.pointRadius,
            0,
            2 * Math.PI,
            false
          );
          context.fill();
          context.closePath();

          // position for next segment
          context.beginPath();
          context.moveTo(point.x * this.scaleX, point.y * this.scaleY);
        }
        context.restore();
      };

      LineChart.prototype.transformContext = function () {
        var context = this.context;

        // move context to center of canvas
        this.context.translate(this.x, this.y + this.height);

        // invert the y scale so that that increments
        // as you move upwards
        context.scale(1, -1);
      };

      function task1() {
        var myLineChart = new LineChart({
          canvasId: "task1",
          minX: 0,
          minY: 0,
          maxX: 31,
          maxY: 100,
          unitsPerTickX: 1,
          unitsPerTickY: 10,
        });
        function getData() {
          var xhttp = new XMLHttpRequest();

          xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
              var obj = JSON.parse(xhttp.response);
              var dateData = obj.rates;
              var cRates = [];
              var avg = 0;
              var data = [];
              var date = Object.keys(dateData);
              for (var i = 1; i < 32; i++) {
                cRates[i] = dateData[date[i]].INR;
                avg = avg + cRates[i];
              }
              avg = avg / 30;
              for (var j = 1; j < 32; j++) {
                data.push({ x: j, y: cRates[j] });
              }

              myLineChart.drawLine(data, "gold", 1);
              console.log(data);
            }
          };
          xhttp.open("GET", "data.json", true);
          xhttp.send();
        }
        getData();
      };

       function task2() {
        var myLineChart = new LineChart({
          canvasId: "task2",
          minX: 0,
          minY: 0,
          maxX: 31,
          maxY: 100,
          unitsPerTickX: 1,
          unitsPerTickY: 5,
        });
        function getData() {
          var xhttp = new XMLHttpRequest();

          xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
              var obj = JSON.parse(xhttp.response);
              var dateData = obj.rates;
              var cRates = [];
              var data = [];
              var date = Object.keys(dateData);
              for (var i = 1; i < 32; i++) {
                cRates[i] = dateData[date[i]].INR;
              }
              for (var j = 1; j < 32; j++) {
                data.push({ x: j, y: cRates[j] });
              }

              myLineChart.drawLine(data, "gold", 1);
              console.log(data);
              var cRates = [];
              var data = [];
              var date = Object.keys(dateData);
              for (var i = 1; i < 32; i++) {
                cRates[i] = dateData[date[i]].GBP;
              }
              for (var j = 1; j < 32; j++) {
                data.push({ x: j, y: cRates[j] });
              }

              myLineChart.drawLine(data, "blue", 3);
              console.log(data);
            }
          };
          xhttp.open("GET", "data.json", true);
          xhttp.send();
        }
        getData();
      };
  
      window.onload = function () {
        task1();
        task2();
      };
    
    