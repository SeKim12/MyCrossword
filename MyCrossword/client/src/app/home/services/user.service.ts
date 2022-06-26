import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { User } from "../../shared/models/user.model";
import { Observable } from "rxjs";
import { BASE_URL } from "../../shared/constants";

@Injectable({
  providedIn: "root",
})
export class UserService {
  constructor(private http: HttpClient) {}

  getUser(uid: string): Observable<User> {
    return this.http.get<User>(`${BASE_URL}/users/${uid}/`);
  }

  updateUser(uid: string): Observable<any> {
    return this.http.patch(`${BASE_URL}/users/mark_as_visited/`, {
      uid: uid,
    });
  }
}
