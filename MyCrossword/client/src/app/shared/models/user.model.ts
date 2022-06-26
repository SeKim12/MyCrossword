export class User {
  public uid: string;
  public visitNum: number;

  constructor(id: string, visitNum?: number) {
    this.uid = id;
    this.visitNum = visitNum || 0;
  }

  visited() {
    this.visitNum += 1;
  }
}
