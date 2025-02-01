javascript:(function(){
    async function detectStingray() {
        try {
            let response = await fetch("http://localhost:5000/analyze_network");
            let analysis = await response.json();
            
            if (analysis.suspicious) {
                console.warn("🚨 ALERT: Potential Stingray attack detected!");
                
                // Log public IP for verification
                let ipData = await fetch("https://api64.ipify.org?format=json");
                let ipJson = await ipData.json();
                console.log("📡 Public IP:", ipJson.ip);

                // Trigger countermeasures
                await fetch("http://localhost:5000/shutdown", { method: "POST" });
            } else {
                console.log("✅ No anomalies detected.");
            }
        } catch (error) {
            console.error("Error detecting network anomalies:", error);
        }
    }

    detectStingray();
})();
