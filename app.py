import requests
from requests.auth import HTTPBasicAuth
import json

# --- Konfig ---
URL = "https://5e0cad42.databases.neo4j.io/db/5e0cad42/query/v2"
USER = "5e0cad42"
PASSWORD = "v63KNzPpa6atPxoPBlIHGCa0zRBK2EZt165622Xe7Wc"

def run_query(query, params={}):
    payload = {
        "statement": query,
        "parameters": params
    }
    response = requests.post(
        URL,
        auth=HTTPBasicAuth(USER, PASSWORD),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        data=json.dumps(payload)
    )
    if response.status_code in (200, 202):
        return response.json()
    else:
        print("❌ Query gagal")
        print(response.status_code, response.text)
        return None



# === DAFTAR PERTANYAAN & SKILL ===
questions = [
    ("Apakah kamu suka membangun dan memahami jaringan komputer?", "Networking"),
    ("Apakah kamu suka ngoding (Python, C, dll)?", "Programming"),
    ("Apakah kamu nyaman menggunakan Linux?", "Linux"),
    ("Apakah kamu tertarik mendalami keamanan Windows?", "Windows Security"),
    ("Apakah kamu suka menangani insiden keamanan secara langsung?", "Incident Response"),
    ("Apakah kamu penasaran dengan analisis malware?", "Malware Analysis"),
    ("Apakah kamu suka reverse engineering (membongkar software)?", "Reverse Engineering"),
    ("Apakah kamu tertarik dengan keamanan cloud (AWS, Azure, GCP)?", "Cloud Security"),
    ("Apakah kamu suka analisis risiko dan manajemen keamanan?", "Risk Management"),
    ("Apakah kamu tertarik dengan kebijakan keamanan & compliance?", "Security Policy"),
]

def get_career(skill):
    query = """
    MATCH (s:Skill {name: $skill})-[:BUTUH]->(c:Karir)
    RETURN c.name AS karir
    """
    results = run_query(query, {"skill": skill})
    if not results:
        return []
    return [row[0] for row in results["data"]["values"]]

def get_learning_path(career):
    query = """
    MATCH path=(c:Karir {name: $career})-[:REQUIRES|PREREQUISITE*]->(s:Skill)
    RETURN [n IN nodes(path) WHERE n:Skill | n.name] AS path_skills
    """
    results = run_query(query, {"career": career})
    if not results:
        return []
    all_skills = []
    for row in results["data"]["values"]:
        for skill in row[0]:
            if skill not in all_skills:
                all_skills.append(skill)
    return all_skills





# === MAIN PROGRAM ===
def main():
    print("=== Career Path Cybersecurity (Neo4j Aura via HTTP API) ===\n")
    selected_skills = []

    # Tanyakan 10 pertanyaan
    for q, skill in questions:
        ans = input(q + " (y/n): ").strip().lower()
        if ans == "y":
            selected_skills.append(skill)

    if not selected_skills:
        print("\nKamu belum memilih skill apapun. Tidak ada rekomendasi.")
        return

    print("\nSkill yang kamu pilih:", selected_skills)

    # Kumpulkan semua rekomendasi karir
    all_careers = set()
    for skill in selected_skills:
        careers = get_career(skill)
        all_careers.update(careers)

    if not all_careers:
        print("\nBelum ada karir yang cocok.")
        return

    # Tampilkan karir dan learning path
    print("\n=== Rekomendasi Karir + Learning Path ===")
    for career in all_careers:
        path = get_learning_path(career)
        print(f"\nKarir: {career}")
        print("Learning Path:", " → ".join(path))

if __name__ == "__main__":
    main()
