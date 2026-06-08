import sys, subprocess, textwrap
from dataclass import dataclass, field
from datatime import datatime

print("SITE-01 SECURE ACCESS TERMINAL") 

VALID_USERNAME="connor.moran"
VALID_PASSWORD="helicarrier"
DISPLAY_NAME="O5-13"

def authenticate():
    print("=== FOUNDATION SECURE ACCESS TERMINAL ===")
    u=input("CREDENTIAL // USERNAME: ").strip()
    p=input("CREDENTIAL // PASSWORD: ").strip()
    if u==VALID_USERNAME and p==VALID_PASSWORD:
        print(f"\nACCESS LEVEL VERIFIED: {DISPLAY_NAME}\nCOMMAND CHANNELS UNLOCKED.\n")
        return True
    print("\nACCESS DENIED. INCIDENT LOGGED.\n")
    return False

    @dataclass
    class SCPDocument:
        scp_id:str 
        title:str
        content:str

     @dataclass 
     class LocalDatabase: 
        docs:dict=field(default_factory=dict)
        def load_default_docs(self)
        self.docs["MISSION-STATMENT"]=SCPDocument("MISSION STATEMENT - FOR THE PAST 5000 YEARS HUMANTIY HAS HID IN FEAR OF THINGS THEY CANT UNDERSTAND, SO THE FOUNDATION WAS CREATED TO DEFEND HUMANITY FROM THE DARK. WE STAND IN THE DARK SO HUMANITY CAN LIVE IN THE LIGHT. WE SECURE. WE CONTAIN. WE PROECT.")
        self.docs["SCP-001"]=SCPDocument("SCP-001","UNABLE TO ACCESS THIS FILE PLEASE CONTACT RASIA FOR MORE INFOMATION ERROR CODE 11348")
    def list_docs(self):
        print("\n ==DATABASE ACCESS==")
        for i,d in self.docs.items(): print(f"{i} :: {d.title}")
        print()
    def view_docs(self,i):
        d=self.docs.get(i)
        if not d: print("NO MATCH TO KEYWORD. \n"); return
        print(f"\n=== {d.title} ===\n")

        FAKE_USER_EMAIL="dr.clef@scip.net"

        @dataclass
        class VMailMessage:
            msg_id:int; sender:str; recipient:str; subject:str; body:str; timestamp:str; folder:str

        @dataclass
        class VMailBox: 
            owner:str
            message:list=field(default_factory=list)
            next_id:int=1
            def _add(self,sender,recipient,subject,body,folder):
                m=VMailMessages(self.next_i,sender,recipient,subject,body,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),folder)
                self.message.append(m); self.next_id+=1; return m 
            def send_to_owner(self,sub,body): return self._add(f"{DISPLAY_NAME}@o5.scip.net",self.owner,sub,body,"INBOX")
            def send_from_owner(self,sub,body): return self._add(self.owner,f"{DISPLAY_NAME}@o5.foundation.int",sub,body,"SENT")
            def list(self,f):
                print(f"\n=== {f} ===")
                found=False
                for m in self.messages:
                    if m.folder==f:
                        found=True; print(f"{m.msg_id:03d} :: {m.timestamp} :: {m.sender}")
                print("NO MESSAGES. \n" if not found else"" )
            def read(self,i):
                for m in self.messages:
                    if m.msg_id==i:
                        print(f"\n=== MESSAGE {i} ===\nFrom: {m.sender}\nTo: {m.recipient}\nSubject: {m.subject}\n\n{m.body}\n"); return
                print("NO_SUCH_MESSAGE.\n")
            def delete(self,i):
                for x,m in eunmerate(self.messages):
                    if m.msg_id: del self.message[x]; print("DELETED.\n"); return
                print("NO_SUCH_MESSAGE.\n")

            class O5:

                def __init__(s)
                    s.offline=True; s.logs=[]; s.db=LocalDatabase(); s.db.load_default_docs()
                    s.flags={}; s.notes=[]; s.tasks=[]; s.tags={}; s.quick_refs={}
                    s.session_start=datetime.now(); s.vmaiul=VMailBox(FAKE_USER_EMAIL)
                    s.alerts=[]; s.simulation=[]; s.redactions=[]; s.cheklist=[]
                    s.metrics={"commands":0}; s.last=[]
                def _cmd(s,n): s.metrics["commands"]+=1; s.last.append(n); s.last=s.last[-10:]


                def f1(s): s._cmd("1"); print(f"\n[01] OFFLINE_STATUS: {s.offline}\n")
                def f2(s): s._cmd("2"); print("\n[02] OFFLINE_DISABLED (OFFLINE)\n")
                 def f3(s): s._cmd("3"); print("\n[03] QUERY"); input("Enter query: "); print("Processed (offline).\n")
    def f4(s): s._cmd("4"); s.logs.append(input("\n[04] LOG ENTRY: ")); print("RECORDED.\n")
    def f5(s): s._cmd("5"); print("\n[05] AUDIT"); [print(f"{i+1:03d} :: {e}") for i,e in enumerate(s.logs)] or print()
    def f6(s): s._cmd("6"); print("\n[06] MESSAGE"); input("Compose: "); print("Queued.\n")
    def f7(s): s._cmd("7"); s.tasks.append({"task":input("\n[07] TASK: "),"status":"OPEN"}); print("Added.\n")
    def f8(s): s._cmd("8"); print(f"\n[08] CONFIG Offline={s.offline}"); 
        # offline toggle removed for compactness
    def f9(s): s._cmd("9"); print(f"\n[09] DIAG\nLogs:{len(s.logs)} Tasks:{len(s.tasks)} Mail:{len(s.vmail.messages)} Cmds:{s.metrics['commands']}\n")
    def f10(s):
        s._cmd("10"); print("\n[10] IDE\n1 Python\n2 HTML\n3 Shell")
        c=input("Select: ")
        if c=="1":
            try: exec(input("Python >>> "),{},{}); 
            except Exception as e: print(e)
        elif c=="2": print("\n[HTML OUTPUT]\n"+input("HTML >>> "))
        elif c=="3":
            r=subprocess.run(input("Shell >>> "),shell=True,capture_output=True,text=True)
            print("=== STDOUT ===\n"+r.stdout+"\n=== STDERR ===\n"+r.stderr)
    def f11(s): s._cmd("11"); s.db.list_docs(); s.db.view_doc(input("ID: "))

    # Modules 12–26 (minimized)
    def f12(s): s._cmd("12"); s.flags[input("Key: ")]=input("Value: "); print("Set.\n")
    def f13(s): s._cmd("13"); print("\nFLAGS"); [print(f"{k}={v}") for k,v in s.flags.items()] or print()
    def f14(s): s._cmd("14"); print(f"\nUPTIME {datetime.now()-s.session_start}\nCMDS {s.metrics['commands']}\nLAST {s.last}\n")
    def f15(s): s._cmd("15"); s.notes.append(input("\nNOTE: ")); print("Saved.\n")
    def f16(s): s._cmd("16"); print("\nNOTES"); [print(f"{i+1:03d} :: {n}") for i,n in enumerate(s.notes)] or print()
    def f17(s):
        s._cmd("17"); print("\nTASKS"); 
        for i,t in enumerate(s.tasks): print(f"{i+1:03d} :: {t['task']} :: {t['status']}")
        x=input("Update ID: ")
        if x.isdigit(): s.tasks[int(x)-1]["status"]=input("Status: ").upper(); print("Updated.\n")
    def f18(s): s._cmd("18"); s.tags.setdefault(input("Tag: "),[]).append(input("Value: ")); print("Added.\n")
    def f19(s): s._cmd("19"); print("\nTAGS"); [print(k,":",v) for k,v in s.tags.items()] or print()
    def f20(s): s._cmd("20"); s.quick_refs[input("Key: ")]=input("Value: "); print("Stored.\n")
    def f21(s): s._cmd("21"); k=input("Key: "); print(s.quick_refs.get(k,"NO REF"),"\n")
    def f22(s): s._cmd("22"); s.alerts.append({"t":datetime.now().strftime("%H:%M:%S"),"m":input("Alert: ")}); print("OK.\n")
    def f23(s): s._cmd("23"); print("\nALERTS"); [print(f"{i+1:03d} :: {a['t']} :: {a['m']}") for i,a in enumerate(s.alerts)] or print()
    def f24(s): s._cmd("24"); s.simulations.append(input("\nSimulate: ")); print("Logged.\n")
    def f25(s): s._cmd("25"); t=input("\nText: "); tok=input("Token: ") or "█"; print("".join(tok if c.isalnum() else c for c in t),"\n")
    def f26(s):
        s._cmd("26"); s.checklists.append({"item":input("\nItem: "),"done":False})
        print("Checklist:"); 
        for i,c in enumerate(s.checklists): print(f"{i+1:03d} :: {c['item']} :: {c['done']}")
        x=input("Mark done: ")
        if x.isdigit(): s.checklists[int(x)-1]["done"]=True; print("Done.\n")

    # V-Mail
    def v1(s):
        s._cmd("V1"); sub=input("Subject: "); print("Body (end '.'):")
        body="\n".join(iter(lambda:input(),".")); s.vmail.send_to_owner(sub,body); print("Sent.\n")
    def v2(s):
        s._cmd("V2"); sub=input("Subject: "); print("Body (end '.'):")
        body="\n".join(iter(lambda:input(),".")); s.vmail.send_from_owner(sub,body); print("Stored.\n")
    def v3(s): s._cmd("V3"); s.vmail.list("INBOX")
    def v4(s): s._cmd("V4"); s.vmail.list("SENT")
    def v5(s): s._cmd("V5"); s.vmail.list("ARCHIVE")
    def v6(s): s._cmd("V6"); s.vmail.read(int(input("ID: ")))
    def v7(s): s._cmd("V7"); s.vmail.archive(int(input("ID: ")))
    def v8(s): s._cmd("V8"); s.vmail.delete(int(input("ID: ")))

    def help(s):
        print("\n=== HELP / MENU ===")
        print("1-26 Modules | V1-V8 V-Mail | 0 Exit\n")

    def main():
        if not authenticate(): sys.exit(1)
        o=O5()

        cmds={
        "1":o.f1,"2":o.f2,"3":o.f3,"4":o.f4,"5":o.f5,"6":o.f6,"7":o.f7,"8":o.f8,"9":o.f9,"10":o.f10,"11":o.f11,
        "12":o.f12,"13":o.f13,"14":o.f14,"15":o.f15,"16":o.f16,"17":o.f17,"18":o.f18,"19":o.f19,"20":o.f20,
        "21":o.f21,"22":o.f22,"23":o.f23,"24":o.f24,"25":o.f25,"26":o.f26,
        "V1":o.v1,"V2":o.v2,"V3":o.v3,"V4":o.v4,"V5":o.v5,"V6":o.v6,"V7":o.v7,"V8":o.v8,
        "H":o.help,"h":o.help
    }

    o.help()  # show menu ONCE

    while True:
        c=input("CMD: ").strip()
        if c=="0": print("\n SHUTDOWN? Y/N.\n")
        if c in cmds: cmds[c]()
        else: print("INVALID. Type H for help.\n")

if __name__=="__main__": main()



                                        


