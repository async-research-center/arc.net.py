import sys, subprocess, textwrap
from dataclasses import dataclass, field

VALID_USERNAME = "connor.moran"
VALID_PASSWORD = "helicarrier"
DISPLAY_NAME = "O5-13"


def authenticate():
    print("=== FOUNDATION SECURE ACCESS TERMINAL ===")
    u = input("CREDENTIAL // USERNAME: ").strip()
    p = input("CREDENTIAL // PASSWORD: ").strip()
    if u == VALID_USERNAME and p == VALID_PASSWORD:
        print(f"\nACCESS LEVEL VERIFIED: {DISPLAY_NAME}")
        print("COMMAND CHANNELS UNLOCKED.\n")
        return True
    print("\nACCESS DENIED. INCIDENT LOGGED.\n")
    return False


@dataclass
class SCPDocument:
    scp_id: str
    title: str
    content: str


@dataclass
class LocalDatabase:
    docs: dict = field(default_factory=dict)

    def load_default_docs(self):
        self.docs["SCP-001"] = SCPDocument(
            "SCP-001",
            "Special Containment Procedures – SCP-001",
            textwrap.dedent(
                """
                ===== SCP‑001 FULL DOCUMENT =====
                Document Type: SCP File
                Clearance Level: 4
                Classification: Euclid

                Object Class: Euclid
                Special Containment Procedures:
                SCP‑001 is contained within a reinforced archival chamber at Site‑09, outfitted with humidity‑controlled storage racks and a triple‑layer electromagnetic shielding array. Access is restricted to personnel with Level‑4 clearance or higher. All interactions must be logged, and no more than one researcher may handle SCP‑001 at a time. Handling requires insulated gloves and a protective visor to mitigate exposure to the emitted photonic discharge.

                The chamber must remain under continuous surveillance. Any fluctuation in SCP‑001’s luminosity exceeding 12% must trigger an automatic lockdown and alert the Site Director. Under no circumstances may SCP‑001 be removed from its containment chamber without written authorization from O5 Command. Digital replication attempts are strictly prohibited following Incident 001‑A.

                Description:
                SCP‑001 is a leather‑bound manuscript of unknown origin, measuring approximately 32 cm by 24 cm. The pages emit a soft, pale‑blue luminescence that intensifies when the object is opened. The light does not appear to originate from any chemical or mechanical source; instead, it behaves as a coherent photonic field that reacts to cognitive focus. Subjects reading SCP‑001 report a sensation of “being observed,” though no external entity has been detected.

                The text within SCP‑001 is written in a shifting script that adapts to the reader’s primary language. Linguistic analysis shows that the content is not static; passages rearrange themselves between readings, and entire sections may appear or disappear. Despite this, all recorded readings share a thematic focus on memory, loss, and the preservation of knowledge.

                Extended exposure to SCP‑001 has measurable cognitive effects. Subjects report heightened recall, increased pattern recognition, and a persistent compulsion to continue reading. After approximately 40 minutes of exposure, subjects begin experiencing intrusive recollections of events they do not remember experiencing. These recollections are vivid, emotionally charged, and often involve unfamiliar individuals or locations.

                Addendum 001‑A:
                During a routine examination, Researcher Halden attempted to photograph SCP‑001’s pages. The resulting digital file corrupted instantly, overwriting nearby storage sectors with repeating strings of text resembling SCP‑001’s script. The affected system displayed a continuous error message: “ARCHIVE MUST BE PRESERVED.” All equipment involved was quarantined and later incinerated.

                Addendum 001‑B — Discovery:
                SCP‑001 was recovered from the ruins of a private library in northern Greece following a seismic event. Local authorities reported an “unusual glow” emanating from beneath collapsed stonework. Foundation agents embedded in the region secured the object and administered amnestics to all witnesses. No records of the library’s ownership or construction have been found.

                ===== END OF DOCUMENT =====
                """
            ),
        )
        self.docs["SCP-002"] = SCPDocument(
            "SCP-002",
            "Special Containment Procedures – SCP-002",
            textwrap.dedent(
                """
                ===== SCP‑002 FULL DOCUMENT =====
                Document Type: SCP File
                Clearance Level: 4
                Classification: Keter

                Object Class: Keter
                Special Containment Procedures:
                SCP‑002 is housed in a sealed acoustic isolation chamber at Site‑41. The chamber walls are lined with triple‑density sound‑absorption foam and vibration‑dampening plates. Entry requires Level‑4 authorization and must be conducted in pairs. No personnel may remain inside the chamber for more than five minutes.

                All communication devices are prohibited within 20 meters of SCP‑002’s containment area. Any detected audio anomalies—defined as unexplained voices, repeated phrases, or sounds resembling personnel—must be reported immediately. If SCP‑002 attempts vocal contact, personnel are instructed to ignore all auditory stimuli and exit the chamber without responding.

                Description:
                SCP‑002 is an empty rectangular room measuring 6.2 m by 4.8 m. The interior walls are composed of an unidentified composite material that absorbs 99.8% of sound. Despite this, SCP‑002 regularly produces auditory phenomena, including whispers, footsteps, and full‑sentence vocalizations. These sounds do not originate from any identifiable source within the room.

                The vocalizations frequently mimic the voices of Foundation personnel, often repeating phrases spoken earlier in the day. In several cases, SCP‑002 has produced accurate imitations of individuals who were not present on‑site. The phenomenon appears to be cumulative; the more personnel exposed to SCP‑002, the broader its vocal repertoire becomes.

                Subjects exposed to SCP‑002 for more than three minutes begin experiencing auditory hallucinations outside the chamber. These hallucinations typically manifest as familiar voices calling their name or urging them to return to SCP‑002. Prolonged exposure leads to increased anxiety, sleep disruption, and, in rare cases, dissociation.

                Addendum 002‑A — Incident Report:
                During a scheduled inspection, SCP‑002 produced a vocalization matching the voice of Dr. Lorne, who had been deceased for six months. The voice repeated the phrase “I’m still here” for approximately 47 seconds. All personnel present reported intense discomfort and a sensation of being watched. Following this incident, SCP‑002’s classification was upgraded to Keter.

                Addendum 002‑B — Hypothesis:
                Acoustic analysis suggests SCP‑002 does not generate sound through vibration. Instead, the auditory phenomena appear to be cognitively targeted, manifesting directly within the auditory cortex of nearby individuals. Research is ongoing.

                ===== END OF DOCUMENT =====
                """
            ),
        )
        self.docs["SCP-003"] = SCPDocument(
            "SCP-003",
            "Special Containment Procedures – SCP-003",
            textwrap.dedent(
                """
                ===== SCP‑003 FULL DOCUMENT =====
                Document Type: SCP File
                Clearance Level: 4
                Classification: Thaumiel

                Object Class: Thaumiel
                Special Containment Procedures:
                SCP‑003 is maintained within a climate‑controlled greenhouse at Site‑77. Access is restricted to personnel with Level‑4 clearance or higher. All maintenance must be performed using non‑metallic tools to prevent mechanical interference. The greenhouse must be inspected daily for structural anomalies, spontaneous growth events, or mechanical activity.

                Any new growths must be catalogued, photographed, and analyzed before removal. Under no circumstances may SCP‑003 material be taken off‑site without O5 authorization. Personnel interacting with SCP‑003 must undergo weekly psychological evaluations to monitor for anomalous influence.

                Description:
                SCP‑003 is a biomechanical ecosystem composed of plant‑like organisms constructed from brass, copper, and crystalline components. Despite lacking organic tissue, SCP‑003 exhibits growth patterns identical to terrestrial flora. Leaves unfold through precise mechanical articulation, and metallic vines extend along predetermined paths, guided by internal clockwork mechanisms.

                The ecosystem is self‑sustaining. SCP‑003 absorbs ambient heat and converts it into kinetic energy, powering its internal mechanisms. At night, the structure emits a soft ticking sound, synchronized across all components. This ticking has been shown to reduce stress and stabilize heart rate in nearby subjects.

                SCP‑003 demonstrates limited adaptive behavior. When exposed to environmental stressors—such as temperature shifts or physical damage—the system reconfigures itself, redistributing mechanical components to maintain structural integrity. In one documented case, SCP‑003 produced a new lattice of copper “roots” to reinforce a weakened support beam.

                Addendum 003‑A — Interaction Log:
                During a controlled experiment, SCP‑003 extended a vine toward Researcher Imani’s hand. The vine paused approximately 2 cm from contact, then retracted. Subsequent analysis revealed the vine’s gears had shifted into a configuration resembling a scanning mechanism. SCP‑003 has since repeated this behavior with multiple researchers.

                Addendum 003‑B — Thaumiel Classification Justification:
                SCP‑003’s ability to self‑repair, adapt, and stabilize environmental conditions has proven invaluable in the development of containment infrastructure. Prototype containment chambers incorporating SCP‑003‑derived components have shown a 37% reduction in structural failure rates. As such, SCP‑003 has been designated Thaumiel and approved for limited integration into high‑risk containment systems.

                ===== END OF DOCUMENT =====
                """
            ),
        )

    def list_docs(self):
        print("\n=== LOCAL SCP DATABASE INDEX ===")
        for i, d in self.docs.items():
            print(f"{i} :: {d.title}")
        print()

    def view_doc(self, i):
        d = self.docs.get(i)
        if not d:
            print("NO MATCHING DOCUMENT FOUND.\n")
            return
        print(f"\n=== {d.title} ===\n")
        print(d.content)
        print()


class O5:
    def __init__(s):
        s.offline = True
        s.logs = []
        s.db = LocalDatabase()
        s.db.load_default_docs()

    def f1(s):
        print("\n[MODULE 01] OFFLINE CAPABILITY STATUS")
        print(f"Offline mode: {s.offline}\n")

    def f2(s):
        print("\n[MODULE 02] ONLINE CAPABILITY (STUB)\n")

    def f3(s):
        print("\n[MODULE 03] KNOWLEDGE BASE QUERY")
        q = input("Enter query: ")
        print(f"Query received: {q}\n")

    def f4(s):
        print("\n[MODULE 04] LOGGING SYSTEM")
        e = input("Enter log entry: ")
        s.logs.append(e)
        print("ENTRY RECORDED.\n")

    def f5(s):
        print("\n[MODULE 05] AUDIT TRAIL")
        if not s.logs:
            print("NO LOGS.\n")
            return
        for i, e in enumerate(s.logs, 1):
            print(f"{i:03d} :: {e}")
        print()

    def f6(s):
        print("\n[MODULE 06] MESSAGING")
        m = input("Compose message: ")
        print(f"Message queued: {m}\n")

    def f7(s):
        print("\n[MODULE 07] TASK QUEUE")
        t = input("Describe task: ")
        print(f"Task registered: {t}\n")

    def f8(s):
        print("\n[MODULE 08] CONFIG")
        print(f"Offline: {s.offline}")
        if input("Toggle offline? (y/n): ") == "y":
            s.offline = not s.offline
            print(f"Offline now: {s.offline}\n")

    def f9(s):
        print("\n[MODULE 09] DIAGNOSTICS")
        print(f"Offline: {s.offline}")
        print(f"Logs: {len(s.logs)}")
        print(f"SCP docs: {len(s.db.docs)}\n")

    def f10(s):
        print("\n[MODULE 10] IDE/TERMINAL")
        print("1) Python")
        print("2) HTML")
        print("3) Shell")
        c = input("Select: ")
        if c == "1":
            code = input("Python >>> ")
            try:
                exec(code, {}, {})
            except Exception as e:
                print(e)
        elif c == "2":
            h = input("HTML >>> ")
            print("\n[HTML OUTPUT]\n" + h)
        elif c == "3":
            cmd = input("Shell >>> ")
            try:
                r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                print("=== STDOUT ===")
                print(r.stdout)
                print("=== STDERR ===")
                print(r.stderr)
            except Exception as e:
                print(e)
        print()

    def f11(s):
        print("\n[MODULE 11] SCP DATABASE")
        s.db.list_docs()
        s.db.view_doc(input("Enter SCP ID: "))

    def help(s):
        print("\n=== HELP INDEX ===")
        print("1 Offline")
        print("2 Online")
        print("3 Knowledge")
        print("4 Log")
        print("5 Audit")
        print("6 Message")
        print("7 Task")
        print("8 Config")
        print("9 Diagnostics")
        print("10 IDE")
        print("11 SCP DB")
        print("H Help")
        print("0 Exit\n")


def main():
    if not authenticate():
        sys.exit(1)
    o = O5()
    a = {
        "1": o.f1,
        "2": o.f2,
        "3": o.f3,
        "4": o.f4,
        "5": o.f5,
        "6": o.f6,
        "7": o.f7,
        "8": o.f8,
        "9": o.f9,
        "10": o.f10,
        "11": o.f11,
        "h": o.help,
        "H": o.help,
    }
    while True:
        print("=== O5 COMMAND CONSTRUCT ===")
        print(f"ACTIVE OPERATOR: {DISPLAY_NAME}")
        print("1 Offline")
        print("2 Online")
        print("3 Knowledge")
        print("4 Log")
        print("5 Audit")
        print("6 Message")
        print("7 Task")
        print("8 Config")
        print("9 Diagnostics")
        print("10 IDE")
        print("11 SCP DB")
        print("H Help")
        print("0 Exit")
        c = input("SELECT MODULE: ").strip()
        if c == "0":
            print("\nSESSION TERMINATED.\n")
            break
        if c in a:
            a[c]()
        else:
            print("INVALID.\n")


if __name__ == "__main__":
    main()
