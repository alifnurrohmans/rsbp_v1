// Karir
CREATE (red:Karir {name:"Red Team Specialist"})
CREATE (blue:Karir {name:"Blue Team Specialist"})
CREATE (soc:Karir {name:"SOC Analyst"})
CREATE (pentest:Karir {name:"Penetration Tester"})
CREATE (forensic:Karir {name:"Digital Forensic Investigator"})

// Skill / Minat
CREATE (net:Skill {name:"Networking"})
CREATE (prog:Skill {name:"Programming"})
CREATE (linux:Skill {name:"Linux"})
CREATE (win:Skill {name:"Windows Security"})
CREATE (incident:Skill {name:"Incident Response"})
CREATE (malware:Skill {name:"Malware Analysis"})
CREATE (reverse:Skill {name:"Reverse Engineering"})
CREATE (cloud:Skill {name:"Cloud Security"})
CREATE (risk:Skill {name:"Risk Management"})
CREATE (policy:Skill {name:"Security Policy"})

// Relasi Skill -> (networking butuh untuk soc analyst)
// butuh -> wajib memiliki skill itu!
CREATE (net)-[:BUTUH]->(soc)
CREATE (prog)-[:BUTUH]->(pentest)
CREATE (linux)-[:BUTUH]->(pentest)
CREATE (incident)-[:BUTUH]->(blue)
CREATE (malware)-[:BUTUH]->(forensic)
CREATE (reverse)-[:BUTUH]->(red)
CREATE (cloud)-[:BUTUH]->(blue)
CREATE (risk)-[:BUTUH]->(blue)
CREATE (policy)-[:BUTUH]->(soc)

// Learning Path (urutan skill)
// Makna requires : starting point skill tertentu untuk masuk ke learning path.
// Makna pre : Skill A prasyarat untuk belajar Skill B.
CREATE (pentest)-[:REQUIRES]->(net)
CREATE (net)-[:PREREQUISITE]->(linux)
CREATE (linux)-[:PREREQUISITE]->(prog)
CREATE (prog)-[:PREREQUISITE]->(reverse)

CREATE (soc)-[:REQUIRES]->(net)
CREATE (net)-[:PREREQUISITE]->(incident)
CREATE (incident)-[:PREREQUISITE]->(cloud)

CREATE (forensic)-[:REQUIRES]->(win)
CREATE (win)-[:PREREQUISITE]->(malware)
CREATE (malware)-[:PREREQUISITE]->(reverse)

// kalau mau nambah red / blue path learning : 
// Blue Team Specialist learning path
CREATE (blue)-[:REQUIRES]->(incident)
CREATE (incident)-[:PREREQUISITE]->(cloud)
CREATE (cloud)-[:PREREQUISITE]->(risk)
CREATE (risk)-[:PREREQUISITE]->(policy)

// Red Team Specialist learning path
CREATE (red)-[:REQUIRES]->(prog)
CREATE (prog)-[:PREREQUISITE]->(reverse)
CREATE (reverse)-[:PREREQUISITE]->(linux)
CREATE (linux)-[:PREREQUISITE]->(net)

// update merge : 
// Learning Path untuk Blue Team Specialist (karena harus ada 1 requires minimal untuk bisa jadi sebuah path)
MATCH (blue:Karir {name:"Blue Team Specialist"}),
      (net:Skill {name:"Networking"}),
      (incident:Skill {name:"Incident Response"}),
      (cloud:Skill {name:"Cloud Security"}),
      (risk:Skill {name:"Risk Management"}),
      (policy:Skill {name:"Security Policy"})
MERGE (blue)-[:REQUIRES]->(net)
MERGE (net)-[:PREREQUISITE]->(incident)
MERGE (incident)-[:PREREQUISITE]->(cloud)
MERGE (cloud)-[:PREREQUISITE]->(risk)
MERGE (risk)-[:PREREQUISITE]->(policy);

// red team
MERGE (pentestSkill:Skill {name: "Penetration Testing"})
MERGE (exploitSkill:Skill {name: "Exploitation"})
MERGE (reverse:Skill {name: "Reverse Engineering"})
MERGE (red:Karir {name: "Red Team Specialist"})
MERGE (red)-[:REQUIRES]->(pentestSkill)
MERGE (red)-[:REQUIRES]->(exploitSkill)
MERGE (red)-[:REQUIRES]->(reverse);



