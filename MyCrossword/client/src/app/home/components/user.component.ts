import { Component, Input } from "@angular/core";
import { User } from "../../shared/models/user.model";
import { UserService } from "../services/user.service";
import { catchError, Observable, of, throwError } from "rxjs";

@Component({
  selector: "app-user",
  templateUrl: "./user.component.html",
  styleUrls: ["./user.component.css"],
  providers: [UserService],
})
export class UserComponent {
  @Input() uid!: string;
  @Input() display: boolean = false;
  user$!: Observable<User>;
  constructor(private service: UserService) {}

  // when user not found, create default user
  // this is not persisted into the database until updateUser
  getUser() {
    this.user$ = this.service
      .getUser(this.uid)
      .pipe(catchError(() => of(new User(this.uid, 0))));
  }

  updateUser() {
    this.service
      .updateUser(this.uid)
      .pipe(catchError(e => throwError(e)))
      .subscribe();
  }
}
